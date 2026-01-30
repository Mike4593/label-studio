"""
FSM state choices registry system.

This module provides the infrastructure for registering and managing
state choices for different entity types in the FSM framework.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from fsm.registry import register_state_choices

"""
Core state choice enums for Label Studio entities.
These enums define the essential states for core Label Studio entities.
"""

# TODO : update
@register_state_choices('task')
class TaskStateChoices(models.TextChoices):
    """
    Extended task states with review pipeline support.
    Workflow: CREATED → IN_PROGRESS → SUBMITTED → PENDING_REVIEW → FINALIZED
    Alternative: PENDING_REVIEW → REJECTED → IN_PROGRESS (reassigned)
    """

    # Initial State
    CREATED = 'CREATED', _('Created')

    # Work States
    IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
    SUBMITTED = 'SUBMITTED', _('Submitted for Review')
    PENDING_REVIEW = 'PENDING_REVIEW', _('Pending Review')

    # Final States
    FINALIZED = 'FINALIZED', _('Finalized')
    REJECTED = 'REJECTED', _('Rejected')

@register_state_choices('annotation')
class AnnotationStateChoices(models.TextChoices):
    """Annotations don't carry state in LSO, but this can still be used for tracking history."""

    CREATED = 'CREATED', _('Created')


@register_state_choices('project')
class ProjectStateChoices(models.TextChoices):
    """
    Core project states for basic Label Studio workflow.
    Simplified states covering the essential project lifecycle:
    - Setup and configuration
    - Active work
    - Completion
    """

    # Setup States
    CREATED = 'CREATED', _('Created')

    # Work States
    IN_PROGRESS = 'IN_PROGRESS', _('In Progress')

    # Terminal State
    COMPLETED = 'COMPLETED', _('Completed')
